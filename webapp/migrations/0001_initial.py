# Generated by Django 4.0.4 on 2022-05-15 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowerRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('thumbnail_url', models.URLField(max_length=2083)),
                ('cropped_thumbnail_url', models.URLField(max_length=2083)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ('-width', '-updated_at'),
            },
        ),
        migrations.CreateModel(
            name='ImageBase64',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2200, unique=True)),
                ('base64', models.TextField(blank=True, db_index=True, editable=False, null=True, unique=True)),
                ('image', models.ImageField(blank=True, editable=False, null=True, upload_to='images')),
                ('filename', models.CharField(blank=True, editable=False, max_length=2200, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'ImagesB64',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2200)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('shortcode', models.CharField(db_index=True, max_length=100, unique=True)),
                ('taken_at', models.PositiveIntegerField()),
                ('comments_count', models.PositiveIntegerField()),
                ('likes_count', models.PositiveIntegerField()),
                ('filter_type', models.PositiveSmallIntegerField(default=0)),
                ('media_type', models.PositiveSmallIntegerField(default=1)),
                ('original_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('original_height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('caption_is_edited', models.BooleanField(default=False)),
                ('is_paid_partnership', models.BooleanField(default=False)),
                ('comment_likes_enabled', models.BooleanField(default=False)),
                ('is_unified_video', models.BooleanField(default=False)),
                ('is_post_live', models.BooleanField(default=False, null=True)),
                ('commerciality_status', models.CharField(default='not_commericial', max_length=30)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('caption', models.CharField(blank=True, max_length=2200, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', related_query_name='has_post', to='webapp.location')),
            ],
            options={
                'verbose_name_plural': 'posts',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='ScrapingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=400, unique=True)),
                ('scraped_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('taken_at', models.PositiveIntegerField()),
                ('expiring_at', models.PositiveIntegerField()),
                ('is_video', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'stories',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('has_audio', models.BooleanField()),
                ('video_duration', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('view_count', models.IntegerField(blank=True, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', related_query_name='has_video', to='webapp.post')),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', related_query_name='has_video', to='webapp.story')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'ordering': ('-width', '-updated_at'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('username', models.CharField(db_index=True, max_length=30, unique=True)),
                ('posts_count', models.PositiveIntegerField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic_url', models.URLField(blank=True, max_length=2083, null=True)),
                ('profile_pic_url_hd', models.URLField(blank=True, max_length=2083, null=True)),
                ('external_url', models.URLField(blank=True, max_length=2083, null=True)),
                ('fbid', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('biography', models.CharField(blank=True, max_length=200, null=True)),
                ('followers', models.PositiveIntegerField(blank=True, null=True)),
                ('following', models.PositiveIntegerField(blank=True, null=True)),
                ('is_business_account', models.BooleanField(default=False)),
                ('is_professional_account', models.BooleanField(default=False)),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('connected_fb_page', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('follower', models.ManyToManyField(related_name='follows', through='webapp.FollowerRelation', to='webapp.user')),
            ],
            options={
                'verbose_name_plural': 'InstaUsers',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story', related_query_name='has_story', to='webapp.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', related_query_name='has_post', to='webapp.user'),
        ),
        migrations.AddConstraint(
            model_name='location',
            constraint=models.UniqueConstraint(fields=('lng', 'lat'), name='loc_unique'),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', related_query_name='has_image', to='webapp.post'),
        ),
        migrations.AddField(
            model_name='image',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', related_query_name='has_image', to='webapp.story'),
        ),
        migrations.AddField(
            model_name='highlight',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlight', related_query_name='has_highlight', to='webapp.user'),
        ),
        migrations.AddField(
            model_name='followerrelation',
            name='from_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='webapp.user'),
        ),
        migrations.AddField(
            model_name='followerrelation',
            name='to_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='webapp.user'),
        ),
    ]
