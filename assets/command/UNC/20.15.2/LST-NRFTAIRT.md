---
id: UNC@20.15.2@MMLCommand@LST NRFTAIRT
type: MMLCommand
name: LST NRFTAIRT（查询TAI路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFTAIRT
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
- TAI路由管理
status: active
---

# LST NRFTAIRT（查询TAI路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的TAI路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：全网规划<br>取值范围：<br>- SMF（SMF）<br>- AMF（AMF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为SMF、AMF、NWDAF的路由转发功能，其他NF类型为预留功能。 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| TACSTART | TAC起始字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC起始字符。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| TACEND | TAC结束字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC结束字符。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于TAI寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFTAIRT]] · TAI路由（NRFTAIRT）

## 使用实例

- 查询所有的TAI路由：
  ```
  LST NRFTAIRT:;
  %%LST NRFTAIRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型  移动国家码  移动网号  TAC起始字符  TAC结束字符  归属NRF组名称  

  SMF     123         456       000001       000100       L-NRF1    
  SMF     123         567       000101       000200       L-NRF2    
  AMF     123         678       000501       000600       L-NRF3    
  (结果个数 = 3)
  ```
- 查询指定NF类型的TAI路由信息。例如，在H-NRF上，查询NF类型为SMF、MCC为123、MNC为456的TAI路由信息。
  ```
  LST NRFTAIRT: NFTYPE=SMF, MCC="123", MNC="456";
  %%LST NRFTAIRT: NFTYPE=SMF, MCC="123", MNC="456";%%
  RETCODE = 0  操作成功

  结果如下
  --------
         NF类型  =  SMF
     移动国家码  =  123
       移动网号  =  456
    TAC起始字符  =  000001
    TAC结束字符  =  000100
  归属NRF组名称  =  L-NRF1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TAI路由（LST-NRFTAIRT）_09653255.md`
