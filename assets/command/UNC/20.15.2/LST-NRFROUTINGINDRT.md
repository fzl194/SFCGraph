---
id: UNC@20.15.2@MMLCommand@LST NRFROUTINGINDRT
type: MMLCommand
name: LST NRFROUTINGINDRT（查询选路指示器路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFROUTINGINDRT
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
- 选路指示器路由管理
status: active
---

# LST NRFROUTINGINDRT（查询选路指示器路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的选路指示器路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在当前NRF上通过选路指示器路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- AUSF（AUSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AUSF的路由转发功能，其他NF类型为预留功能。 |
| ROUTINGIND | 选路指示器 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0~9999。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFROUTINGINDRT]] · 选路指示器路由（NRFROUTINGINDRT）

## 使用实例

- 查询所有的选路指示器路由：
  ```
  LST NRFROUTINGINDRT:;
  %%LST NRFROUTINGINDRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型  选路指示器  归属NRF组名称  

  UDM     1111        L-NRF1         
  AUSF    1111        L-NRF1         
  (结果个数 = 2)
  ```
- 查询指定NF类型的路由信息。例如，在H-NRF上，查询NF类型为UDM的选路指示器及该NF归属的L-NRF实例组名称。
  ```
  LST NRFROUTINGINDRT: NFTYPE=UDM;
  %%LST NRFROUTINGINDRT: NFTYPE=UDM;%%
  RETCODE = 0  操作成功

  结果如下
  --------
         NF类型 = UDM
     选路指示器 = 1111
  归属NRF组名称 = H-NRF1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询选路指示器路由（LST-NRFROUTINGINDRT）_09652642.md`
