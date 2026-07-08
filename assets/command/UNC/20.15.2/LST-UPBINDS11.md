---
id: UNC@20.15.2@MMLCommand@LST UPBINDS11
type: MMLCommand
name: LST UPBINDS11（查询SGW-U与SGW-C侧S11接口的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPBINDS11
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定S11接口
status: active
---

# LST UPBINDS11（查询SGW-U与SGW-C侧S11接口的绑定关系）

## 功能

**适用NF：SGW-C**

该命令用于查询SGW-U与SGW-C侧S11接口的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | SGW-U实例名称 | 可选必选说明：可选参数<br>参数含义：该参数标识SGW-U实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该对象最大实例数为100条。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SGW-U与SGW-C侧S11接口的绑定关系（UPBINDS11）](configobject/UNC/20.15.2/UPBINDS11.md)

## 使用实例

- 查询所有的SGW-U与S11口的绑定关系： LST UPBINDS11:;
  ```
  %%LST UPBINDS11:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  SGW-U实例名称  S11口地址类型  S11口IPv4地址  S11口IPv6地址  S11口优先级 

  upf1           IPv4           192.168.1.2    ::             2             
  upf1           IPv4           192.168.10.2   ::             3             
  (结果个数 = 2)
  ```
- 查询指定条件的SGW-U与S11口的绑定关系，比如查询UPF唯一标识为“UPF1”的SGW-U与S11口绑定关系： LST UPBINDS11: NFINSTANCENAME="UPF1";
  ```
  %%LST UPBINDS11: NFINSTANCENAME="UPF1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  SGW-U实例名称  =  upf1
  S11口地址类型  =  IPv4
  S11口IPv4地址  =  192.168.10.2
  S11口IPv6地址  =  ::
    S11口优先级  =  3
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW-U与SGW-C侧S11接口的绑定关系（LST-UPBINDS11）_09652520.md`
