---
id: UNC@20.15.2@MMLCommand@LST PGWCHARACT
type: MMLCommand
name: LST PGWCHARACT（查询P-GW特性对接配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWCHARACT
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
- GnGp-GGSN_S5_S8接口管理
- P-GW属性
status: active
---

# LST PGWCHARACT（查询P-GW特性对接配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询需要匹配的对端P-GW的属性信息。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PGWCHARACT]] · P-GW特性对接配置（PGWCHARACT）

## 使用实例

1. 查询所有记录：
  LST PGWCHARACT:;

  ```
  %%LST PGWCHARACT:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
                           对端设备范围  =  指定IP的P-GW
                             IP地址类型  =  IPv4
                               IPv4地址  =  10.141.196.197
                           IPv4地址掩码  =  255.255.255.0
                         P-GW支持MME ID  =  不支持
      是否向P-GW转发LTE-M类型的RAT TYPE  =  不支持
  P-GW支持P-CSCF Restoration Indication  =  不支持
  仍有后续报告输出
  ---    END
  %%LST PGWCHARACT:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
                           对端设备范围  =  指定IP的P-GW
                             IP地址类型  =  IPv6
                               IPv6地址  =  2001:db8:10:19:44:55:10:12
                       IPv6地址前缀长度  =  120
                         P-GW支持MME ID  =  不支持
      是否向P-GW转发LTE-M类型的RAT TYPE  =  不支持
  P-GW支持P-CSCF Restoration Indication  =  不支持
  (结果个数 = 2)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PGWCHARACT.md`
