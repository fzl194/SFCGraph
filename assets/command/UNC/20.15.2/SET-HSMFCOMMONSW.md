---
id: UNC@20.15.2@MMLCommand@SET HSMFCOMMONSW
type: MMLCommand
name: SET HSMFCOMMONSW（设置H-SMF通用控制开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HSMFCOMMONSW
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- H-SMF会话管理拓展功能
status: active
---

# SET HSMFCOMMONSW（设置H-SMF通用控制开关）

## 功能

**适用NF：SMF**

该命令用于设置H-SMF通用控制开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SERVINGNODEIPSW |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVINGNODEIPSW | 服务节点IP地址开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制SEPP组网场景下，N40接口消息是否不携带服务节点IP地址。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：<br>当该参数值为ENABLE时，SEPP组网场景下，N40接口消息不携带服务节点IP地址；<br>当该参数值为DISABLE时，N40接口消息携带服务节点IP地址为SEPP地址；<br>该参数仅在servingNode改变后立即生效。 |

## 操作的配置对象

- [H-SMF通用控制开关（HSMFCOMMONSW）](configobject/UNC/20.15.2/HSMFCOMMONSW.md)

## 使用实例

设置H-SMF通用控制开关：

```
SET HSMFCOMMONSW: SERVINGNODEIPSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置H-SMF通用控制开关（SET-HSMFCOMMONSW）_46482137.md`
