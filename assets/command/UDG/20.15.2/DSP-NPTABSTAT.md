---
id: UDG@20.15.2@MMLCommand@DSP NPTABSTAT
type: MMLCommand
name: DSP NPTABSTAT（查询NP表项简要信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPTABSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP资源管理
- NP资源信息查询
- NP表项信息
status: active
---

# DSP NPTABSTAT（查询NP表项简要信息）

## 功能

该命令用于查询指定RU上NP表项的简要信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- Tunnel-IPV4、Tunnel-IPV6资源仅包含GRE资源，不包括IPSEC资源。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无。<br>配置原则：使用<br>[DSP RU](../../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询RU编号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPTABSTAT]] · NP表项简要信息（NPTABSTAT）

## 使用实例

显示RUID为68的NP表项简要信息：

DSP NPTABSTAT: RUID=68;

```
RETCODE = 0  操作成功

结果如下
--------
表名称           表索引  子表索引  资源总数  已分配资源  

FIB-IPV4         8       0         524288    6           
FIB-IPV6         9       0         524288    0           
BFD              14      1         4096      3           
NDH              15      0         65536     0           
ARP              14      0         131072    0           
Tunnel-IPV4      19      8         4096      0           
Tunnel-IPV6      16      8         4096      0           
TBL_NST_FE_IID4  178     0         262144    0           
TBL_NST_FE_IID6  184     0         262144    0           
TBL_NHP_IID4     132     0         196608    0           
TBL_NHP_IID6     144     0         196608    0           
ND               52      0         65536     0           
(结果个数 = 12)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NPTABSTAT.md`
