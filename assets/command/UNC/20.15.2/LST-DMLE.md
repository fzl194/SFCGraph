---
id: UNC@20.15.2@MMLCommand@LST DMLE
type: MMLCommand
name: LST DMLE（查询Diameter本端实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMLE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
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

# LST DMLE（查询Diameter本端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于查询当前的Diameter本端实体信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的Diameter本地实体的索引。<br>取值范围：0～31<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMLE]] · Diameter本端实体（DMLE）

## 使用实例

查询Diameter本地实体信息：

LST DMLE: LOINDEX=0;

```
%%LST DMLE: LOINDEX=0;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  本地实体索引  =  0
本地实体主机名  =  mme.epc.mnc123.mcc123.3gppnetwork.org
  本地实体域名  =  epc.mnc123.mcc123.3gppnetwork.org
        产品名  =  MME
    本地实体名  =  DMLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMLE.md`
