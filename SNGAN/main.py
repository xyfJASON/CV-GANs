import argparse

from trainer import Trainer
from tester import Tester


def train(config_path):
    assert config_path
    trainer = Trainer(config_path)
    trainer.train()


def walk(model_path, z_dim, img_channels, save_path):
    assert model_path and z_dim and img_channels and save_path
    tester = Tester(model_path, z_dim, img_channels)
    tester.walk_in_latent_space(save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['train', 'walk'])
    parser.add_argument('--config_path', help='train')
    parser.add_argument('--model_path', help='walk')
    parser.add_argument('--z_dim', type=int, help='walk')
    parser.add_argument('--img_channels', type=int, help='walk')
    parser.add_argument('--save_path', help='walk')
    args = parser.parse_args()

    if args.mode == 'train':
        train(args.config_path)
    elif args.mode == 'walk':
        walk(args.model_path, args.z_dim, args.img_channels, args.save_path)
    else:
        raise ValueError