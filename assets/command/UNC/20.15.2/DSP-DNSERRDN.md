---
id: UNC@20.15.2@MMLCommand@DSP DNSERRDN
type: MMLCommand
name: DSP DNSERRDN（查询失败的DNS记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DNSERRDN
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
- DNS
- DNS Cache管理
status: active
---

# DSP DNSERRDN（查询失败的DNS记录）

## 功能

**适用网元：SGSN、MME**

该命令用于查询 UNC 检查出的DNS错误域名信息。导致这些错误的原因包括DNS服务器配置错误、配置不完整等。当 UNC 检测出有DNS查询失败时，会将相关信息记录在系统中，使用该命令可以查询出相关错误信息；当 UNC 检测出DNS查询成功后，再将相关错误信息从系统中清除。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ERRTYPE | 错误类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定要查询的错误类型。<br>数据来源：本端规划<br>取值范围：<br>- “SVR_RSP_FAIL（服务器响应失败）”<br>- “SERVICE_MISS（服务名称缺失）”<br>默认值：无<br>说明：- “服务器响应失败”，表示服务器返回查询失败。<br>- “服务名称缺失”，表示DNS服务器或者UNC本地没有配置业务需要的网元类型、接口类型、S5/S8接口协议类型。 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定要查询的SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：1~63 位字符串<br>默认值：无 |
| PROCESSNO | 进程号 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定要查询的SPP的进程序号。通过<br>[**DSP PROCESSUSN**](../../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询USN进程信息(DSP PROCESSUSN)_11295773.md)<br>获取。<br>前提条件：该参数在<br>“错误类型”<br>参数配置为<br>“服务名称缺失”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~20<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：需要填写LINK_VNFC或USN_VNFC对应的名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSERRDN]] · 失败的DNS记录（DNSERRDN）

## 使用实例

显示错误类型为SVR_RSP_FAIL的DNS错误域名信息：

DSP DNSERRDN: ERRTYPE=SVR_RSP_FAIL,SERVICETYPE="USN_VNFC";

```
%%DSP DNSERRDN: ERRTYPE=SVR_RSP_FAIL,
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下:
-------------------------
                          DNS域名  =  HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
                         查询类型  =  NAPTR类型查询
                         错误类型  =  服务器响应失败
                     域名信息来源  =  DNS 服务器
                     失败参考信息  =  HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
             第一次查询失败的时间  =  2017-01-20 14:57:04
           最近一次查询失败的时间  =  2017-01-20 14:57:04
                     查询失败次数  =  1
(结果数目 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DNSERRDN.md`
