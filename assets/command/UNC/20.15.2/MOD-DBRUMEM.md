---
id: UNC@20.15.2@MMLCommand@MOD DBRUMEM
type: MMLCommand
name: MOD DBRUMEM（修改CSDB RU内存信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DBRUMEM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 内存管理
status: active
---

# MOD DBRUMEM（修改CSDB RU内存信息）

## 功能

![](修改CSDB RU内存信息(MOD DBRUMEM)_04873821.assets/notice_3.0-zh-cn_2.png)

该操作将修改CSDB RU上数据备份内存大小，不合理的修改将导致CSDB异常，修改后需要重启CSDB生效。

该命令用于修改CSDB RU内存信息。

## 注意事项

- 执行该命令之前，请先确保存在RU内存信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLUSTERTYPE | 集群类型 | 可选必选说明：必选参数<br>参数含义: 该参数用于指定集群类型，分为普通集群和XSF集群。<br>数据来源：本端规划<br>取值范围：<br>- “COMMON_CLUSTER”：普通集群。<br>- “XSF_CLUSTER”：XSF集群。<br>默认值：无<br>配置原则：无 |
| RUTYPE | RU类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU类型，可以通过<br>**[DSP RU](../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md): SERVICEINSTANCE="CSDB_VNFC_999";**<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| MEMSIZE | 内存大小(G) | 可选必选说明：必选参数。<br>参数含义：该参数用于设定RU的内存大小。<br>数据来源：本端规划<br>取值范围：整型，0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBRUMEM]] · CSDB RU内存信息（DBRUMEM）

## 使用实例

修改 **“集群类型”** 为 “COMMON_CLUSTER” ，“ **RU类型** ”为“CSDB_SD_RU”的RU内存大小为5G：

```
MOD DBRUMEM: CLUSTERTYPE=COMMON_CLUSTER, RUTYPE="CSDB_SD_RU", MEMSIZE=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CSDB-RU内存信息(MOD-DBRUMEM)_04873821.md`
