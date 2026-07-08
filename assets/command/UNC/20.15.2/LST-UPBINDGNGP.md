---
id: UNC@20.15.2@MMLCommand@LST UPBINDGNGP
type: MMLCommand
name: LST UPBINDGNGP（查询GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPBINDGNGP
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定GnGp或S5S8接口
status: active
---

# LST UPBINDGNGP（查询GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系）

## 功能

**适用NF：GGSN、PGW-C**

该命令用于查询GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | GGSN或PGW-U实例名称 | 可选必选说明：可选参数<br>参数含义：该参数标识GGSN或PGW-U实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该对象最大实例数为100条。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPBINDGNGP]] · GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系（UPBINDGNGP）

## 使用实例

- 查询所有的GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系： LST UPBINDGNGP:;
  ```
  %%LST UPBINDGNGP:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  GGSN或PGW-U实例名称  Gn/Gp或S5/S8口地址类型  Gn/Gp或S5/S8口IPv4地址  Gn/Gp或S5/S8口IPv6地址  Gn/Gp或S5/S8口优先级

  upf1                 IPv4                    192.168.1.2             ::                      0
  upf2                 IPv4                    192.168.10.2            ::                      0  
  (结果个数 = 2)
  ```
- 查询指定条件的GGSN与Gn/Gp接口或PGW-U与S5/S8接口的绑定关系，比如查询UPF唯一标识为“UPF1”的GGSN与Gn/Gp接口绑定关系 LST UPBINDGNGP: NFINSTANCENAME="UPF1";
  ```
  %%LST UPBINDGNGP: NFINSTANCENAME="UPF1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
     GGSN或PGW-U实例名称  =  upf1
  Gn/Gp或S5/S8口地址类型  =  IPv4
  Gn/Gp或S5/S8口IPv4地址  =  192.168.10.2
  Gn/Gp或S5/S8口IPv6地址  =  ::
    Gn/Gp或S5/S8口优先级  =  3
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPBINDGNGP.md`
