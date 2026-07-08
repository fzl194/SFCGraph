---
id: UNC@20.15.2@MMLCommand@DSP FABRICSUBHEALTHY
type: MMLCommand
name: DSP FABRICSUBHEALTHY（显示FABRIC内联口亚健康信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FABRICSUBHEALTHY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# DSP FABRICSUBHEALTHY（显示FABRIC内联口亚健康信息）

## 功能

该命令用于显示Fabric平面亚健康信息。

## 注意事项

- 该命令执行后立即生效。
- 此命令显示两个资源之间的链路亚健康信息，Bonding模式不支持基于链路的亚健康统计，在Bonding模式下此命令无回显结果。可以使用[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)命令查看是否Bonding模式。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| REMOTERETB | 远端节点TB | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端节点的资源ID。<br>数据来源：本端规划<br>取值范围：整数类型，0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FABRICSUBHEALTHY]] · FABRIC内联口亚健康信息（FABRICSUBHEALTHY）

## 使用实例

- 显示微服务类型为“aa”微服务实例为“aa”的亚健康信息：
  ```
  DSP FABRICSUBHEALTHY:CELLTYPE="aa", CELLINSTANCE="aa";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  本端节点TB  远端节点TB   本端端口名称   远端端口名称     是否亚健康    丢包率（‰）    错包率（‰）    亚健康值 

  1035         1034             eth1           eth1             FALSE         0               0               0   
  1035         1034             eth2           eth2             FALSE         0               0               0
  (结果个数 = 2)
  ---    END
  ```
- 显示微服务类型为“aa”微服务实例为“aa”到远端资源“1034”的亚健康信息：
  ```
  DSP FABRICSUBHEALTHY:CELLTYPE="aa", CELLINSTANCE="aa",REMOTERETB=1034;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  本端节点TB  远端节点TB   本端端口名称   远端端口名称     是否亚健康    丢包率（‰）    错包率（‰）    亚健康值 

  1035         1034             eth1           eth1             FALSE         0               0               0   
  1035         1034             eth2           eth2             FALSE         0               0               0
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FABRICSUBHEALTHY.md`
