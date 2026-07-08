---
id: UNC@20.15.2@MMLCommand@DSP DMLE
type: MMLCommand
name: DSP DMLE（显示Diameter本端实体）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMLE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter本地实体
status: active
---

# DSP DMLE（显示Diameter本端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于查询当前的Diameter本地实体信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的本地实体索引。<br>取值范围：0～31<br>默认值：无<br>说明：不设置该参数，表示查询所有记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLE]] · Diameter本端实体（DMLE）

## 使用实例

查询本地实体状态：

DSP DMLE:;

```
%%DSP DMLE:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
本地实体索引  =  0
  本地实体名  =  DMLE
    实体状态  =  正常
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DMLE.md`
