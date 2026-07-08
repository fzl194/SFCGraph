---
id: UNC@20.15.2@MMLCommand@LST NRFPLMNVISITPLY
type: MMLCommand
name: LST NRFPLMNVISITPLY（查询指定归属地PLMN的拜访地策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPLMNVISITPLY
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

# LST NRFPLMNVISITPLY（查询指定归属地PLMN的拜访地策略）

## 功能

**适用NF：NRF**

该命令用于查询NRF作为拜访地NRF时对指定归属地PLMN的跨PLMN请求处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定归属地PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定归属地PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPLMNVISITPLY]] · 指定归属地PLMN的拜访地策略（NRFPLMNVISITPLY）

## 使用实例

- 查询所有指定归属地PLMN的拜访地策略；
  ```
  %%LST NRFPLMNVISITPLY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                  移动国家码  =  460
                    移动网号  =  03
          是否支持跨PLMN订阅  =  打开
    订阅是否进行Location改造  =  是
        订阅转发是否删除PLMN  =  是
  跨PLMN转发是否剥离目的PLMN  =  是
  (结果个数 = 1)

  ---    END
  ```
- 查询移动国家码为460，移动网号为03的指定归属地PLMN的拜访地策略。
  ```
  %%LST NRFPLMNVISITPLY: MCC="460", MNC="03";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                  移动国家码  =  460
                    移动网号  =  03
          是否支持跨PLMN订阅  =  打开
    订阅是否进行Location改造  =  是
        订阅转发是否删除PLMN  =  是
  跨PLMN转发是否剥离目的PLMN  =  是
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPLMNVISITPLY.md`
