---
id: UNC@20.15.2@MMLCommand@LST NRFBSFIPV4REL
type: MMLCommand
name: LST NRFBSFIPV4REL（查询BSF索引和IPv4的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBSFIPV4REL
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

# LST NRFBSFIPV4REL（查询BSF索引和IPv4的关联关系）

## 功能

**适用NF：NRF**

该命令用于查询BSF索引和IPv4的关联关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| START | IP起始地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv4起始地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>IPv4地址必须是A、B或者C类地址。 |
| END | IP结束地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv4结束地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>IPv4地址必须是A、B或者C类地址。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFBSFIPV4REL]] · BSF索引和IPv4的关联关系（NRFBSFIPV4REL）

## 使用实例

- 查询所有BSF索引和IPv4的关联关系。
  ```
  LST NRFBSFIPV4REL:;
  %%LST NRFBSFIPV4REL:;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
  BSF索引  IP结束地址     IP结束地址
  1        192.168.10.12  192.168.20.12
  2        192.168.10.23  192.168.10.35
  (结果个数 = 2)
  ```
- 查询BSF索引为1的IPv4的关联关系。
  ```
  LST NRFBSFIPV4REL:BSFINDEX=1;
  %%LST NRFBSFIPV4REL:BSFINDEX=1;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
          BSF索引  =  1
       IP起始地址  =  192.168.10.12
       IP结束地址  =  192.168.20.12
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和IPv4的关联关系（LST-NRFBSFIPV4REL）_45612432.md`
