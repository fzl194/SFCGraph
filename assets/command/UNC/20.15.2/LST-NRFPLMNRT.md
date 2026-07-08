---
id: UNC@20.15.2@MMLCommand@LST NRFPLMNRT
type: MMLCommand
name: LST NRFPLMNRT（查询PLMN路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPLMNRT
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
- PLMN路由管理
status: active
---

# LST NRFPLMNRT（查询PLMN路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的PLMN路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示PLMN路由信息的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示PLMN路由信息的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于PLMN寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPLMNRT]] · PLMN路由（NRFPLMNRT）

## 使用实例

- 查询所有PLMN的路由：
  ```
  LST NRFPLMNRT:;
  %%LST NRFPLMNRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  移动国家码  移动网号  归属东西向NRF组名称  
  123         456       L-NRF1          
  123         789       H-NRF1         
  (结果个数 = 2)
  ```
- 查询移动国家码为123，移动网号为456的PLMN路由：
  ```
  LST NRFPLMNRT: MCC="123", MNC="456";
  %%LST NRFPLMNRT: MCC="123", MNC="456";%%
  RETCODE = 0  操作成功

  结果如下
  --------
           移动国家码  =  123
             移动网号  =  456
  归属东西向NRF组名称  =  L-NRF1 
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPLMNRT.md`
