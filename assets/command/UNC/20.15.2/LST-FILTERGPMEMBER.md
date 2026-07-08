---
id: UNC@20.15.2@MMLCommand@LST FILTERGPMEMBER
type: MMLCommand
name: LST FILTERGPMEMBER（查询过滤器组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FILTERGPMEMBER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 过滤器组成员管理
status: active
---

# LST FILTERGPMEMBER（查询过滤器组成员）

## 功能

**适用NF：SMF**

该命令用于查询系统中已有的过滤器信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGPID | 过滤组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤器从属过滤组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。该参数应该与LST FILETERGP命令查询结果中FILTERGPID的值保持一致。<br>默认值：无<br>配置原则：无 |
| DIRECTION | 方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定此过滤器的过滤方向。<br>数据来源：全网规划<br>取值范围：<br>- “DownLink（下行）”：从网络侧到用户侧的数据流方向<br>- “UpLink（上行）”：从用户侧到网络侧的数据流方向<br>- “Bidirectional（双向）”：用户侧与网络侧之间互相传输的数据流方向<br>默认值：无<br>配置原则：无 |
| FILTERTYPE | 过滤器类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤器类型。<br>数据来源：全网规划<br>取值范围：<br>- Ipv4（IPv4）<br>- Ipv6（IPv6）<br>默认值：无<br>配置原则：无 |
| REMOTEIPV4 | 远端IPv4 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv4"时为条件可选参数。<br>参数含义：该参数用于指定远端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| REMOTEIPV6 | 远端IPv6 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv6"时为条件可选参数。<br>参数含义：该参数用于指定远端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| UEIPV4 | UE IPv4 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv4"时为条件可选参数。<br>参数含义：该参数用于指定UE的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| UEIPV6 | UE IPv6 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv6"时为条件可选参数。<br>参数含义：该参数用于指定UE的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILTERGPMEMBER]] · 过滤器组成员（FILTERGPMEMBER）

## 使用实例

- 查询所有的过滤器：
  ```
  %%LST FILTERGPMEMBER:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    过滤组ID  =  1
        方向  =  上行
  过滤器类型  =  IPv4
    远端IPv4  =  172.16.0.1
    远端IPv6  =  ::
     UE IPv4  =  192.168.0.1
     UE IPv6  =  ::
  (结果个数 = 1)

    ------      END
  ```
- 查询指定条件的过滤器，比如查询过滤组ID为1的所有过滤器：
  ```
  %%LST FILTERGPMEMBER: FILTERGPID=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    过滤组ID  =  1
        方向  =  下行
  过滤器类型  =  IPv4
    远端IPv4  =  192.168.0.1
    远端IPv6  =  ::
     UE IPv4  =  192.168.111.111
     UE IPv6  =  ::
  (结果个数 = 1)

    ------      END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询过滤器组成员（LST-FILTERGPMEMBER）_09651746.md`
