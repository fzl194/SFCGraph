---
id: UNC@20.15.2@MMLCommand@LST NRFGUAMIRT
type: MMLCommand
name: LST NRFGUAMIRT（查询GUAMI路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFGUAMIRT
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
- GUAMI路由管理
status: active
---

# LST NRFGUAMIRT（查询GUAMI路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的GUAMI路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成GUAMI的PLMN中移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成GUAMI的PLMN中移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成GUAMI的AMF所在区域标识信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时从左边补0，取值范围0~ff。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成GUAMI的AMF所在集合（即Pool）标识信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时从左边补0，取值范围0~3ff。<br>默认值：无<br>配置原则：无 |
| AMFPOINTER | AMF指示符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成GUAMI的AMF Pionter信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x。不足两位时从左边补0。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于GUAMI寻址AMF时的下一条NRF实例组名称，被寻址的AMF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFGUAMIRT]] · GUAMI路由（NRFGUAMIRT）

## 使用实例

- 查询所有GUAMI路由：
  ```
  LST NRFGUAMIRT:;
  %%LST NRFGUAMIRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  移动国家码     移动网号  AMF区域标识  AMF集合标识  AMF指示符  归属NRF组名称  

  123            456       09           102          12         L-NRF1      
  123            567       08           101          11         L-NRF2       
  (结果个数 = 2)
  ```
- 查询移动国家码为123的GUAMI路由：
  ```
  LST NRFGUAMIRT: MCC="123";
  %%LST NRFGUAMIRT: MCC="123";%%
  RETCODE = 0  操作成功

  结果如下
  --------
     移动国家码  =  123
       移动网号  =  456
    AMF区域标识  =  09
    AMF集合标识  =  102
      AMF指示符  =  12
  归属NRF组名称  =  L-NRF1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GUAMI路由（LST-NRFGUAMIRT）_09654421.md`
