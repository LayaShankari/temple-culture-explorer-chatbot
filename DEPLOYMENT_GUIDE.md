# 🚀 Deployment Guide: Temple Culture Explorer to Hugging Face Spaces

This guide walks you through deploying your Temple Culture Explorer chatbot to Hugging Face Spaces in just a few minutes!

## Prerequisites

✅ Hugging Face account (free at https://huggingface.co/join)
✅ Git installed on your machine
✅ Your Temple Culture Explorer files ready

## Option 1: Deploy via Web Interface (Easiest)

### Step 1: Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in the details:
   - **Owner**: Your username
   - **Space name**: `temple-culture-explorer` (or your choice)
   - **Description**: "A RAG chatbot for exploring Indian temples"
   - **License**: `openrail` (or your choice)
   - **SDK**: Select **Streamlit**
   - **Visibility**: Select **Public**
3. Click **"Create Space"**

### Step 2: Upload Your Files

Via web UI:
1. Open your new Space
2. Click the **"Add file"** button
3. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `.gitignore`
   - Entire `data/` folder
   - `.streamlit/config.toml`

Or via Git (see Option 2 below)

### Step 3: Add OpenAI Secret (Optional)

If you want to use OpenAI API:
1. Click the **⚙️ Settings** button
2. Go to **"Repository secrets"**
3. Click **"Add Secret"**
4. Name: `OPENAI_API_KEY`
5. Value: Paste your OpenAI API key (from https://platform.openai.com/account/api-keys)
6. Click **"Add Secret"**

### Step 4: Done! 🎉

Your Space will automatically deploy. Visit your Space URL to see it live!

---

## Option 2: Deploy via Git (Recommended for Developers)

### Step 1: Create a New Space

Go to [huggingface.co/new-space](https://huggingface.co/new-space) and create your Space (same as Option 1, Step 1).

### Step 2: Clone the Space Repository

```bash
git clone https://huggingface.co/spaces/YOUR-USERNAME/temple-culture-explorer
cd temple-culture-explorer
```

Replace `YOUR-USERNAME` with your actual username.

### Step 3: Copy Your Files

Copy all your files to the cloned directory:

```bash
# Copy main files
cp /path/to/app.py .
cp /path/to/requirements.txt .
cp /path/to/.gitignore .

# Copy data directory
cp -r /path/to/data/ .

# Copy streamlit config
mkdir -p .streamlit
cp /path/to/.streamlit/config.toml .streamlit/
```

### Step 4: Commit and Push

```bash
git add .
git commit -m "Initial commit: Temple Culture Explorer"
git push
```

If prompted for credentials, use:
- **Username**: Your Hugging Face username
- **Password**: Your Hugging Face API token (from https://huggingface.co/settings/tokens)

### Step 5: Add OpenAI Secret (Optional)

In your Space settings on the HF website:
1. Click **⚙️ Settings** (gear icon)
2. Go to **"Repository secrets"**
3. Add `OPENAI_API_KEY` with your OpenAI API key

### Step 6: Done! 🎉

Your Space will automatically deploy within seconds!

---

## Option 3: Deploy via Hugging Face CLI

### Step 1: Install Hugging Face CLI

```bash
pip install huggingface-hub
```

### Step 2: Login

```bash
huggingface-cli login
```

Enter your Hugging Face API token when prompted.

### Step 3: Create and Push Space

```bash
huggingface-cli repo create temple-culture-explorer --type space --space-sdk streamlit --private False

cd temple-culture-explorer
cp /path/to/app.py .
cp /path/to/requirements.txt .
# ... copy other files

git add .
git commit -m "Initial commit"
git push
```

---

## Updating Your Space

### Via Git

```bash
cd temple-culture-explorer
# Make your changes
git add .
git commit -m "Update: Add new temple data"
git push
```

### Via Web UI

1. Open your Space
2. Click **"Files"** tab
3. Click **"Add file"** to upload new files
4. The Space will redeploy automatically

---

## Environment Variables & Secrets

### For OpenAI Integration:

Set `OPENAI_API_KEY` in your Space settings:

```
Settings → Repository secrets → Add Secret
Name: OPENAI_API_KEY
Value: sk-... (your OpenAI API key)
```

You can optionally set:

```
OPENAI_MODEL = "gpt-3.5-turbo"  # default
# or "gpt-4" for better quality
```

---

## Sharing Your Space

Once deployed, you can:

1. **Share the URL**: `https://huggingface.co/spaces/YOUR-USERNAME/temple-culture-explorer`
2. **Embed in a website**: Get the embed code from Space settings
3. **Link on social media**: Add the Space link to your profile

---

## Troubleshooting

### Issue: Space won't start / shows errors

**Solution:**
1. Check the **"Logs"** tab in your Space for error messages
2. Verify `requirements.txt` has correct package names
3. Ensure `app.py` exists and has correct syntax
4. Make sure `data/` folder is included

### Issue: OpenAI API not working

**Solution:**
1. Verify `OPENAI_API_KEY` is set in Repository secrets (not just `secrets.toml`)
2. Check your OpenAI API key has remaining credits
3. Try without OpenAI first—the app works perfectly without it!

### Issue: Knowledge base not loading

**Solution:**
1. Check that `data/` folder exists with `.txt` or `.md` files
2. Verify file paths in the code are correct
3. Click "Reload knowledge base" in the sidebar
4. Check Streamlit logs for errors

### Issue: Slow responses

**Solution:**
1. Reduce `top_k` slider in the sidebar
2. Reduce document file sizes
3. Optimize TF-IDF parameters in `app.py`

---

## After Deployment: Next Steps

### 1. Add More Content

Add new temple files to `data/`:

```bash
# Add a new temple
echo "Somnath Temple, Gujarat

Historic temple dedicated to Lord Shiva..." > data/somnath_temple_new.txt

git add data/somnath_temple_new.txt
git commit -m "Add more temples"
git push
```

### 2. Customize UI

Edit `.streamlit/config.toml` to change:
- Colors (primaryColor, backgroundColor, etc.)
- Font
- Page layout

### 3. Monitor Usage

In Space settings:
- View statistics about visitors
- Check logs for errors
- Monitor resource usage

### 4. Upgrade Your Space

- **Community Support**: Get help on HF forums
- **Persistent Storage**: Keep data between restarts
- **Custom Domain**: Link a custom domain

---

## File Checklist ✅

Before pushing, ensure you have:

- [ ] `app.py` - Main application
- [ ] `requirements.txt` - Dependencies
- [ ] `README.md` - Documentation
- [ ] `.gitignore` - What to exclude
- [ ] `data/` folder - Knowledge base files
- [ ] `.streamlit/config.toml` - Streamlit config
- [ ] `.streamlit/` folder created

---

## Resources

- 📚 [Streamlit Docs](https://docs.streamlit.io/)
- 🤗 [HF Spaces Docs](https://huggingface.co/spaces)
- 🔑 [OpenAI API](https://platform.openai.com/)
- 💬 [HF Community Forum](https://discuss.huggingface.co/)

---

## Need Help?

- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Review [HF Spaces guides](https://huggingface.co/docs/hub/spaces)
- Ask questions in [HF Community](https://discuss.huggingface.co/)

---

**Happy deploying! 🚀**
