---
id: UNC@20.15.2@MMLCommand@LST NRFREGIDSETIDREL
type: MMLCommand
name: LST NRFREGIDSETIDREL（查询AMF区域标识和集合标识的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFREGIDSETIDREL
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
- AMF区域标识路由管理
status: active
---

# LST NRFREGIDSETIDREL（查询AMF区域标识和集合标识的关联关系）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询AMF区域标识和集合标识的关联关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFREGID | AMF区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF区域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时从左边补0，取值范围0~ff。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF集合标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时从左边补0，取值范围0~3ff。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF区域标识所归属的当前NRF的下一跳路由归属的NRF实例组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFREGIDSETIDREL]] · AMF区域标识和集合标识的关联关系（NRFREGIDSETIDREL）

## 使用实例

- 查询AMF区域标识09为集合标识为123的关联关系：
  ```
  LST NRFREGIDSETIDREL: AMFREGID="09", AMFSETID="123",NEXTNRFGRPNAME="nrfgroup001";
  %%LST NRFREGIDSETIDREL: AMFREGID="09", AMFSETID="123",NEXTNRFGRPNAME="nrfgroup001";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    AMF区域标识  =  09
    AMF集合标识  =  123
  归属NRF组名称  =  nrfgroup001
  (结果个数 = 1)
  ```
- 查询全部AMF区域标识和集合标识的关联关系：
  ```
  LST NRFREGIDSETIDREL:;
  %%LST NRFREGIDSETIDREL:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  AMF区域标识  AMF集合标识  归属NRF组名称

  09           123          nrfgroup001
  10           056          nrfgroup002
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFREGIDSETIDREL.md`
