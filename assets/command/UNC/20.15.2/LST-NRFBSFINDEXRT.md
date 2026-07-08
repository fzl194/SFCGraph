---
id: UNC@20.15.2@MMLCommand@LST NRFBSFINDEXRT
type: MMLCommand
name: LST NRFBSFINDEXRT（查询BSFINDEX路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBSFINDEXRT
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

# LST NRFBSFINDEXRT（查询BSFINDEX路由）

## 功能

**适用NF：NRF**

该命令用于查询选择BSF时的路由实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于BSF类型寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFBSFINDEXRT]] · BSFINDEX路由（NRFBSFINDEXRT）

## 使用实例

- 查询所有的选择BSF时的路由实例信息：
  ```
  LST NRFBSFINDEXRT:;
  %%LST NRFBSFINDEXRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  BSF索引  归属NRF组名称
  1        L-NRF1
  1        H-NRF1
  (结果个数 = 2)
  ```
- 查询BSF索引为1，归属NRF组名称为H-NRF1的路由信息：
  ```
  LST NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";
  %%LST NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        BSF索引  =  1
  归属NRF组名称  =  H-NRF1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSFINDEX路由（LST-NRFBSFINDEXRT）_44007034.md`
