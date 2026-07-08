---
id: UDG@20.15.2@MMLCommand@DSP SIGNATUREDB
type: MMLCommand
name: DSP SIGNATUREDB（查询协议特征库文件加载状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SIGNATUREDB
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- 识别特征库
status: active
---

# DSP SIGNATUREDB（查询协议特征库文件加载状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询系统中存有的知识库的信息，包括知识库版本和引擎版本。引擎是编译版本的时候固化的，网元版本不变、引擎就不会变化。知识库是不定期更新的，为了适应现网环境下各种协议软件的变化，知识库不断升级。

例如：msn新推出14.0版本，用旧知识库识别率可能只会有80％；只升级知识库可以将识别率提高到100％。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [协议特征库文件（SIGNATUREDB）](configobject/UDG/20.15.2/SIGNATUREDB.md)

## 使用实例

查询知识库信息：

```
DSP SIGNATUREDB:;
```

```

RETCODE = 0  操作成功。

协议识别特征库信息
------------------
特征库加载模式  =  更新为最新的特征库版本
  特征库版本号  =  01.0002.1071.01
特征库加载状态  =  加载完成
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询协议特征库文件加载状态（DSP-SIGNATUREDB）_82837717.md`
