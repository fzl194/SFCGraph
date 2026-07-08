---
id: UNC@20.15.2@MMLCommand@SET SMFGLBDLBUFTIME
type: MMLCommand
name: SET SMFGLBDLBUFTIME（设置全局下行报文缓存时长）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFGLBDLBUFTIME
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
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

# SET SMFGLBDLBUFTIME（设置全局下行报文缓存时长）

## 功能

**适用NF：SGW-C**

该命令用来配置全局下行报文缓存时长。

## 注意事项

- 该命令执行后立即生效。

- 该命令在不配置SMFAPNDLBUFTIME场景下生效。
- 该命令应与UPF的GLBDLBUFTIME保持一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NORMALUSER | NBIOTUSER |
| --- | --- |
| 6 | 6 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NORMALUSER | 普通用户下行报文缓存时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局的普通用户下行报文缓存时长。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是3~15，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFGLBDLBUFTIME查询当前参数配置值。<br>配置原则：无 |
| NBIOTUSER | NB-IoT用户下行报文缓存时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局的NB-IoT用户下行报文缓存时长。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是3~200，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFGLBDLBUFTIME查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFGLBDLBUFTIME]] · 全局下行报文缓存时长（SMFGLBDLBUFTIME）

## 使用实例

配置全局普通用户下行报文缓存时长，普通用户下行报文缓存时长(秒)为9s：

```
SET SMFGLBDLBUFTIME: NORMALUSER=9;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMFGLBDLBUFTIME.md`
