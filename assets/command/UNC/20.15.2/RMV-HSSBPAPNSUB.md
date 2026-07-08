---
id: UNC@20.15.2@MMLCommand@RMV HSSBPAPNSUB
type: MMLCommand
name: RMV HSSBPAPNSUB（删除HSS BYPASS最小APN签约数据配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HSSBPAPNSUB
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS BYPASS最小签约数据配置管理
status: active
---

# RMV HSSBPAPNSUB（删除HSS BYPASS最小APN签约数据配置）

## 功能

**适用网元：MME**

此命令用于删除最小APN签约数据群组对应的最小APN签约数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN本地签约数据索引。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSBPAPNSUB]] · HSS BYPASS最小APN签约数据配置（HSSBPAPNSUB）

## 使用实例

删除HSS BYPASS最小APN签约数据配置，可以用如下命令：

```
RMV HSSBPAPNSUB: APNSUBIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HSSBPAPNSUB.md`
