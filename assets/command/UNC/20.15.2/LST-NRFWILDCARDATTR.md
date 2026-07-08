---
id: UNC@20.15.2@MMLCommand@LST NRFWILDCARDATTR
type: MMLCommand
name: LST NRFWILDCARDATTR（查询分层互联通配属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFWILDCARDATTR
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
- NRF路由通配属性配置
status: active
---

# LST NRFWILDCARDATTR（查询分层互联通配属性）

## 功能

**适用NF：NRF**

该命令用于在NRF新增分层互联通配属性。

## 注意事项

- 当分层互联属性类型为TAC时，通配的起始位置加通配的长度小于等于6，即MATCHSTART+MATCHLEN<=6。
- 当分层互联属性类型为NFGROUP或SERVINGSCOPE时，通配的起始位置加通配的长度小于等于128，即MATCHSTART+MATCHLEN<=128。
- 当分层互联属性类型为REGIONIDSETID时，通配的起始位置加通配的长度小于等于18，即MATCHSTART+MATCHLEN<=18。
- 当分层互联属性类型为ROUTINGINDICATOR时，通配的起始位置加通配的长度小于等于4，即MATCHSTART+MATCHLEN<=4。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：可选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：<br>每种属性最多只能配置一条分层互联通配属性。 |
| MATCHSTART | 起始位置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通配的起始位置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| MATCHLEN | 通配长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通配的长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [分层互联通配属性（NRFWILDCARDATTR）](configobject/UNC/20.15.2/NRFWILDCARDATTR.md)

## 使用实例

- 运营商查询属性为NRFNFGROUP，通配起始位置为0，通配长度为3，通配类型为省份的分层互联通配属性信息。
  ```
  LST NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP, MATCHSTART=0, MATCHLEN=3;
  %%LST NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP, MATCHSTART=0, MATCHLEN=3;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
             属性  =  NFGROUP
         起始位置  =  0
         通配长度  =  3
  (结果个数 = 1)

  ---    END
  ```
- 运营商查询所有分层互联通配属性信息。
  ```
  LST NRFWILDCARDATTR:;
  %%LST NRFWILDCARDATTR:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  属性     起始位置  通配长度 
  NFGROUP  0         3       
  TAC      1         2         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询分层互联通配属性（LST-NRFWILDCARDATTR）_09652485.md`
