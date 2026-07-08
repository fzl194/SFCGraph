---
id: UNC@20.15.2@MMLCommand@LST NRFPROXYSMF
type: MMLCommand
name: LST NRFPROXYSMF（查询NRF管理的ProxySMF）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPROXYSMF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFPROXYSMF（查询NRF管理的ProxySMF）

## 功能

**适用NF：NRF**

该命令用于查询NRF管理的ProxySMF。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NRF管理的ProxySMF（NRFPROXYSMF）](configobject/UNC/20.15.2/NRFPROXYSMF.md)

## 使用实例

- 查询本NRF管理的所有ProxySMF信息：
  ```
  LST NRFPROXYSMF:;
  %%LST NRFPROXYSMF:;%%
  RETCODE = 0 执行成功

  结果如下
  -------------------------
  NF实例标识               NF名称 

  Nfinstanceid01   ProxySMF01                          
  Nfinstanceid02   ProxySMF01                             
  (结果个数 = 2)
  ```
- 查询NF实例标识为Nfinstanceid01的ProxySMF信息：
  ```
  LST NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";
  %%LST NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF实例标识  =  Nfinstanceid01
      NF名称  =  ProxySMF01
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF管理的ProxySMF（LST-NRFPROXYSMF）_70462553.md`
