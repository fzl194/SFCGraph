---
id: UNC@20.15.2@MMLCommand@RBL LDPSESSION
type: MMLCommand
name: RBL LDPSESSION（重启LDP会话）
nf: UNC
version: 20.15.2
verb: RBL
object_keyword: LDPSESSION
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- 重启LDP会话
status: active
---

# RBL LDPSESSION（重启LDP会话）

## 功能

该命令用于重启一个LDP会话。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令会导致邻居断连。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERID | 对等体的LSR ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ISGRACEFUL | 是否优雅重启 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否优雅重启。设置ISGRACEFUL为TRUE，可以实现对于指定的对等体在重启时业务不中断。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPSESSION]] · LDP会话（LDPSESSION）

## 使用实例

重启一个LDP会话：

```
RBL LDPSESSION:PEERID="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RBL-LDPSESSION.md`
