---
id: UNC@20.15.2@MMLCommand@SET NGAPTIMER
type: MMLCommand
name: SET NGAPTIMER（设置N2定时器参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGAPTIMER
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动管理定时器
status: active
---

# SET NGAPTIMER（设置N2定时器参数）

## 功能

**适用NF：AMF**

该命令用于设置N2定时器参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BCRELEASETIMER |
| --- |
| 4 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BCRELEASETIMER | 基站释放广播会话超时时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定基站主动发起广播会话释放请求后，AMF通知基站释放广播会话需要等待的时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是3~15。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGAPTIMER查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGAPTIMER]] · N2定时器参数（NGAPTIMER）

## 使用实例

设置N2定时器参数，其中广播基站释放超时时长为3秒，执行如下命令：

```
SET NGAPTIMER:BCRELEASETIMER=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置N2定时器参数（SET-NGAPTIMER）_33151729.md`
