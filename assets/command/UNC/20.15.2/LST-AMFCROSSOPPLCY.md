---
id: UNC@20.15.2@MMLCommand@LST AMFCROSSOPPLCY
type: MMLCommand
name: LST AMFCROSSOPPLCY（查询AMF运营商交互策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFCROSSOPPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF漫游功能控制
- AMF跨运营商交互策略管理
status: active
---

# LST AMFCROSSOPPLCY（查询AMF运营商交互策略）

## 功能

**适用NF：AMF**

该命令用于查询本AMF和其它运营商的AMF/MME之间的跨运营商交互策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERMCC | 对端运营商移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要控制交互策略的对端运营商的Serving PLMN中的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| PEERMNC | 对端运营商移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要控制交互策略的对端运营商的Serving PLMN中的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFCROSSOPPLCY]] · AMF跨运营商交互策略（AMFCROSSOPPLCY）

## 使用实例

- 查询本AMF和其它运营商的AMF/MME之间的跨运营商交互策略，执行如下命令：
  ```
  %%LST AMFCROSSOPPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
             对端运营商移动国家码  =  123
               对端运营商移动网号  =  45
  本网用户N14接口跨运营商交互策略  =  是
  本网用户N26接口跨运营商交互策略  =  否
  漫游用户N14接口跨运营商交互策略  =  是
  漫游用户N26接口跨运营商交互策略  =  否
  (结果个数 = 1)

  ---    END
  ```
- 查询本AMF和运营商A的AMF/MME之间的跨运营商交互策略，执行如下命令：
  ```
  %%LST AMFCROSSOPPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
             对端运营商移动国家码  =  123
               对端运营商移动网号  =  45
  本网用户N14接口跨运营商交互策略  =  是
  本网用户N26接口跨运营商交互策略  =  否
  漫游用户N14接口跨运营商交互策略  =  是
  漫游用户N26接口跨运营商交互策略  =  否
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFCROSSOPPLCY.md`
