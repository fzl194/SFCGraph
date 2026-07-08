---
id: UNC@20.15.2@MMLCommand@LST NRFAMFSETIDRT
type: MMLCommand
name: LST NRFAMFSETIDRT（查询AMF集合标识路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFAMFSETIDRT
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
- AMF集合标识路由管理
status: active
---

# LST NRFAMFSETIDRT（查询AMF集合标识路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的AMF集合标识路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFSETID | AMF集合标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF集合标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时从左边补0，取值范围0~3ff。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于AMF集合标识寻址AMF时的下一跳NRF实例组名称，被寻址的AMF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFAMFSETIDRT]] · AMF集合标识路由（NRFAMFSETIDRT）

## 使用实例

- 查询AMF集合标识为086，归属NRF组名称为L-NRF1的AMF集合标识路由信息：
  ```
  LST NRFAMFSETIDRT:AMFSETID="086",NEXTNRFGRPNAME="L-NRF1";
  %%LST NRFAMFSETIDRT: AMFSETID="086", NEXTNRFGRPNAME="L-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    AMF集合标识  =  086
  归属NRF组名称  =  L-NRF1
  (结果个数  = 1)
  ```
- 查询全部AMF集合标识路由信息：
  ```
  LST NRFAMFSETIDRT:;
  %%LST NRFAMFSETIDRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  AMF集合标识  归属NRF组名称 

  086          L-NRF1      
  087          L-NRF2      
  (结果个数  = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFAMFSETIDRT.md`
