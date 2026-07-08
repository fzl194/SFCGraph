---
id: UNC@20.15.2@MMLCommand@DSP GTPCPATHNUM
type: MMLCommand
name: DSP GTPCPATHNUM（显示GTP-C路径个数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPCPATHNUM
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
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径管理
status: active
---

# DSP GTPCPATHNUM（显示GTP-C路径个数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询指定节点的GTP-C路径数目。

## 注意事项

- 该命令执行后立即生效。
- 该命令可用于SPP进程/UPP进程。
- 当“进程类型”未输入时，默认查询UPP进程上的路径数目信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>[**DSP RU**](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTP | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “UPP(UPP)”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的序号。<br>取值范围：0~20<br>默认值：无 |
| QRYTP | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>取值范围：<br>- “MEMORY(内存)”<br>- “DDB(数据库)”<br>默认值：<br>“MEMORY(内存)”<br>说明：内存中的GTP-C路径数目是由本进程创建的路径数。DDB中的GTP-C路径数目是由UPP创建的路径数。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：<br>- 如果要查询SPP进程上的GTPC路径，则SERVICETYPE需要填写USN的名称。<br>- 如果要查询UPP进程上的GTPC路径，则SERVICETYPE需要填写LINK的名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHNUM]] · GTP-C路径个数（GTPCPATHNUM）

## 使用实例

查询资源单元为USN_SP_RU_0064上的V2版本GTP-C路径数目：

DSP GTPCPATHNUM: RUNAME="USN_SP_RU_0064",SERVICETYPE="USN_VNFC";

```
%%DSP GTPCPATHNUM: RUNAME="USN_SP_RU_0064", 
SERVICETYPE="USN_VNFC";
%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                 RU名称 = USN_SP_RU_0064
               进程类型 = UPP
                进程号  = 0
             GTPC路径数 = 1

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示GTP-C路径个数(DSP-GTPCPATHNUM)_26305720.md`
