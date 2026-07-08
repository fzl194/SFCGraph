---
id: UNC@20.15.2@MMLCommand@RMV IPRESOURCE
type: MMLCommand
name: RMV IPRESOURCE（删除IP资源）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPRESOURCE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- IP资源
status: active
---

# RMV IPRESOURCE（删除IP资源）

## 功能

![](删除IP资源（RMV IPRESOURCE）_51174283.assets/notice_3.0-zh-cn_2.png)

- 执行此命令后立即出现IP不通，请谨慎操作。
- 此命令不能动态生效，需要执行“RST VNFC”重启服务，并且删除IP资源可能导致话单业务不可用或话单无法被取走。

**适用NF：NCG**

该命令用于删除已添加的IP资源。

IP资源有四种用途，不同用途情况下，删除的前提条件有如下不同：

1、IP资源用于话单接收：需要先确保该IP资源没有用来接收话单，然后删除与该IP资源相关的路由资源。

2、IP资源仅用于话单分发：需要先删除该IP资源所在的RU上所有分发任务，然后删除与该IP资源相关的路由资源。

3、IP资源仅用于话单备份：需要先删除该IP资源所在的RU上所有备份到第三方服务器/UDN服务器的任务，然后删除与该IP资源相关的路由资源。

4、IP资源用于话单分发和备份：需要先删除该IP资源所在的RU上所有分发任务和备份到第三方服务器/UDN服务器的任务，然后删除与该IP资源相关的路由资源。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 删除IP资源属于危险操作，仅当不需要话单接收、备份、分发功能时才删除该对RU上的IP资源。
- 删除IP资源之前，需要删除与此IP资源相关的话单接收任务、话单分发任务、话单备份任务、话单路由，否则删除操作会失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | IP资源标识 | 可选必选说明：必选参数<br>参数含义：用于表示一个IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPRESOURCE]] · IP资源（IPRESOURCE）

## 使用实例

删除标识为“cdr_backup-distribution”的话单备份分发IP资源，示例如下：

```
RMV IPRESOURCE: IPRID="IP_Ga_CDRReceive_1st";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPRESOURCE.md`
