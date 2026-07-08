---
id: UNC@20.15.2@MMLCommand@LST SMFGLBDLBUFTIME
type: MMLCommand
name: LST SMFGLBDLBUFTIME（查询全局下行报文缓存时长）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFGLBDLBUFTIME
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- GTP会话协议参数管理
- 下行报文缓存时长
status: active
---

# LST SMFGLBDLBUFTIME（查询全局下行报文缓存时长）

## 功能

**适用NF：SGW-C**

该命令用来查询全局下行报文缓存时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFGLBDLBUFTIME]] · 全局下行报文缓存时长（SMFGLBDLBUFTIME）

## 使用实例

查询全局下行报文缓存时长：

```
%%LST SMFGLBDLBUFTIME:;%%
RETCODE = 0 操作成功

结果如下
----------------------------
普通用户下行报文缓存时长(秒)    =  9
NB-IoT用户下行报文缓存时长(秒)  =  6
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFGLBDLBUFTIME.md`
