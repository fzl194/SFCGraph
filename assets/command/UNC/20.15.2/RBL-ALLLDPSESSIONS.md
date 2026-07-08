---
id: UNC@20.15.2@MMLCommand@RBL ALLLDPSESSIONS
type: MMLCommand
name: RBL ALLLDPSESSIONS（重启所有LDP会话）
nf: UNC
version: 20.15.2
verb: RBL
object_keyword: ALLLDPSESSIONS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- 重启LDP会话
status: active
---

# RBL ALLLDPSESSIONS（重启所有LDP会话）

## 功能

该命令用于重启所有的LDP会话。当进行了新的LDP配置时，可以执行此命令使新的配置生效。

![](重启所有LDP会话（RBL ALLLDPSESSIONS）_00601097.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会导致所有邻居断连。如果不是优雅重启，业务流量会中断。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令会导致邻居断连。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISGRACEFUL | 是否优雅重启 | 可选必选说明：可选参数<br>参数含义：该参数用于表示优雅重启标识。设置ISGRACEFUL为TRUE，如果设备具有GR能力并且与邻居建立GR会话（邻居也有GR能力）则业务不删除。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLLDPSESSIONS]] · 重启所有LDP会话（ALLLDPSESSIONS）

## 使用实例

重启所有的LDP会话：

```
RBL ALLLDPSESSIONS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RBL-ALLLDPSESSIONS.md`
