---
id: UNC@20.15.2@MMLCommand@LST NFSELPLCY
type: MMLCommand
name: LST NFSELPLCY（查询目标NF选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFSELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 目标NF选择策略管理
status: active
---

# LST NFSELPLCY（查询目标NF选择策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF在发现和选择其它目标NF时的设备级可选参数控制策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TGTNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识目标NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SMF（SMF）”：SMF<br>- “LMF（LMF）”：LMF<br>- “GMLC（GMLC）”：GMLC<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFSELPLCY]] · 目标NF选择策略（NFSELPLCY）

## 使用实例

- 查询系统中当前配置的SMF发现和选择流程中相关可选参数的策略，执行如下命令：
  ```
  %%LST NFSELPLCY: TGTNFTYPE=LMF;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                    目标NF类型  =  LMF
            请求者网络切片开关  =  否
     是否使用ClientType发现LMF  =  否
    是否使用ClientType发现GMLC  =  否
  HR模式会话请求者网络切片开关  =  否
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的目标NF发现和选择流程中相关可选参数的策略，执行如下命令：
  ```
  %%LST NFSELPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  目标NF类型  请求者网络切片开关  是否使用ClientType发现LMF  是否使用ClientType发现GMLC  HR模式会话请求者网络切片开关

  SMF         否                  否                         否                          否
  LMF         否                  否                         否                          否
  GMLC        否                  否                         否                          否
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFSELPLCY.md`
