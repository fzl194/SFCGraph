---
id: UNC@20.15.2@MMLCommand@LST SGWDNS
type: MMLCommand
name: LST SGWDNS（查询S-GW DNS域名策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWDNS
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
- S11接口管理
- S-GW域名策略
status: active
---

# LST SGWDNS（查询S-GW DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于配置多PLMNID共享时查询S-GW的域名中PLMNID的组装策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS域名类型。<br>取值范围：<br>- “RAI(RAI)”<br>- “TAI(TAI)”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>取值范围：0x00～0xFF<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“TAI(TAI)”<br>时生效。<br>取值范围：0x0000～0xFFFF<br>默认值 ：无 |

## 操作的配置对象

- [S-GW DNS域名策略（SGWDNS）](configobject/UNC/20.15.2/SGWDNS.md)

## 使用实例

1. 不输入查询条件，查询表中全部DNS域名策略的信息：
  LST SGWDNS:;
  ```
  %%LST SGWDNS:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   域名类型  位置区域码  路由区域码  路由区域码范围  跟踪区域码  跟踪区域码范围  移动国家码  移动网号   描述

   TAI       0x0         0x0         0x0             0x1         0x5             111         222        NULL   
   RAI       0x0         0x5         0x5             0x0         0x0             123         03         NULL   
  (结果个数 = 2)

  ---    END
  ```
2. 查询一条跟踪区域码为“1”的DNS域名策略记录：
  LST SGWDNS: DNTYPE=TAI, TAC="0x1";
  ```
  %%LST SGWDNS: DNTYPE=TAI, TAC="0x1";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
        域名类型  =  TAI
      位置区域码  =  0x0
      路由区域码  =  0x0
  路由区域码范围  =  0x0
      跟踪区域码  =  0x1
  跟踪区域码范围  =  0x5
      移动国家码  =  111
        移动网号  =  222
            描述  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S-GW-DNS域名策略（LST-SGWDNS）_26305782.md`
