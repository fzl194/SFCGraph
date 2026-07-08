---
id: UDG@20.15.2@MMLCommand@DSP NPMICCODEPATCHSTATUS
type: MMLCommand
name: DSP NPMICCODEPATCHSTATUS（显示NP微码补丁加载状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPMICCODEPATCHSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP升级管理
- NP微码补丁状态
status: active
---

# DSP NPMICCODEPATCHSTATUS（显示NP微码补丁加载状态）

## 功能

该命令用于显示NP微码补丁加载状态信息。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>配置原则：使用<br>[DSP RU](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询RU编号。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPMICCODEPATCHSTATUS]] · NP微码补丁加载状态（NPMICCODEPATCHSTATUS）

## 使用实例

显示RUID为66的NP卡微码补丁加载状态信息：

```
DSP NPMICCODEPATCHSTATUS:RUID=66;
```

```
RETCODE = 0  操作成功

结果如下
--------
补丁状态  =  未加载        
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NPMICCODEPATCHSTATUS.md`
