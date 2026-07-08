---
id: UNC@20.15.2@MMLCommand@LST NRFIPDOMAINREL
type: MMLCommand
name: LST NRFIPDOMAINREL（查询BSF索引和IP Domain的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFIPDOMAINREL
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

# LST NRFIPDOMAINREL（查询BSF索引和IP Domain的关联关系）

## 功能

**适用NF：NRF**

该命令用于查询已配置的BSF索引和IP Domain的关联关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| IPDOMAIN | IP Domain标识 | 可选必选说明：可选参数<br>参数含义：当SET NRFFUNCSW命令中的IPDOMAINSW开关开启时，该参数用于表示IP Domain后缀；当IPDOMAINSW开关关闭时，该参数用于表示IP Domain标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIPDOMAINREL]] · BSF索引和IP Domain的关联关系（NRFIPDOMAINREL）

## 使用实例

- 查询所有已配置的BSF索引和IP Domain的关联关系信息：
  ```
  LST NRFIPDOMAINREL:;
  %%LST NRFIPDOMAINREL:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  BSF索引 IP Doamin标识
  1       Huawei
  2       Huawei
  (结果个数 = 2)
  ```
- 查询BSF索引为1，IP Domain标识为Huawei关联关系信息：
  ```
  LST NRFIPDOMAINREL:  BSFINDEX=1, IPDOMAIN="Huawei";
  %%LST NRFIPDOMAINREL:  BSFINDEX=1, IPDOMAIN="Huawei";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        BSF索引 = 1
  IP Doamin标识 = Huawei
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFIPDOMAINREL.md`
