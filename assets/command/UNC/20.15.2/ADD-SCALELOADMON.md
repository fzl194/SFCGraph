---
id: UNC@20.15.2@MMLCommand@ADD SCALELOADMON
type: MMLCommand
name: ADD SCALELOADMON（增加自动扩缩容监测的虚机资源）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCALELOADMON
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- VNFC公共功能管理
- 操作维护
- 扩缩容管理
status: active
---

# ADD SCALELOADMON（增加自动扩缩容监测的虚机资源）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于自动扩缩容场景下，开启指定虚机资源的负载监测，并作为虚机自动扩缩容的依据。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOADCATEGORY |
| --- |
| SMSESSIONLOAD |
| AMUSERLOAD |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOADCATEGORY | 自动扩缩容上报资源种类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自动扩缩容上报资源种类。<br>数据来源：本端规划<br>取值范围：<br>- SMSESSIONLOAD（sm-pod的会话资源）<br>- AMUSERLOAD（usn-pod的5G用户资源）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [自动扩缩容监测的虚机资源（SCALELOADMON）](configobject/UNC/20.15.2/SCALELOADMON.md)

## 使用实例

配置一种会话类型的自动扩缩容检测项，执行如下命令：

```
%%ADD SCALELOADMON: LOADCATEGORY=SMSESSIONLOAD;%%
RETCODE = 0  Operation succeeded
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加自动扩缩容监测的虚机资源（ADD-SCALELOADMON）_24015920.md`
