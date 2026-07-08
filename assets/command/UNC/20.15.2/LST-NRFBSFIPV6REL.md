---
id: UNC@20.15.2@MMLCommand@LST NRFBSFIPV6REL
type: MMLCommand
name: LST NRFBSFIPV6REL（查询BSF索引和IPv6的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBSFIPV6REL
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- BSF路由管理
status: active
---

# LST NRFBSFIPV6REL（查询BSF索引和IPv6的关联关系）

## 功能

**适用NF：NRF**

该命令用于查询BSF索引和IPv6的关联关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| START | IP起始地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv6起始地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）。 |
| STARTMASK | 起始IPv6地址的掩码长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv6起始地址的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~128。<br>默认值：无<br>配置原则：无 |
| END | IP结束地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv6结束地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）。 |
| ENDMASK | 结束IPv6地址的掩码长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv6结束地址的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [BSF索引和IPv6的关联关系（NRFBSFIPV6REL）](configobject/UNC/20.15.2/NRFBSFIPV6REL.md)

## 使用实例

- 查询所有BSF索引和IPv6的关联关系。
  ```
  LST NRFBSFIPV6REL:;
  %%LST NRFBSFIPV6REL:;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
  BSF索引  IP结束字符       起始IPv6地址的掩码长度  IP结束字符        结束IPv6地址的掩码长度
  1        2001:0db8::1     64                      2001:0db8::1000   64
  2        2001:0db8::2000  64                      2001:0db8::a000   64
  (结果个数 = 2)
  ```
- 查询BSF索引为1的IPv6的关联关系。
  ```
  LST NRFBSFIPV6REL:BSFINDEX=1;
  %%LST NRFBSFIPV6REL:BSFINDEX=1;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
                 BSF索引  =  1
              IP起始字符  =  2001:0db8::1
  起始IPv6地址的掩码长度  =  64
              IP结束字符  =  2001:0db8::1000
  结束IPv6地址的掩码长度  =  64
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和IPv6的关联关系（LST-NRFBSFIPV6REL）_45612433.md`
