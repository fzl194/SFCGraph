---
id: UNC@20.15.2@MMLCommand@LST NRFDNAIRGNPREF
type: MMLCommand
name: LST NRFDNAIRGNPREF（查询DNAI区域优选规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDNAIRGNPREF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF区域优选管理
status: active
---

# LST NRFDNAIRGNPREF（查询DNAI区域优选规则）

## 功能

**适用NF：NRF**

该命令用于查询DNAI区域优选规则。该命令功能暂不生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络名称。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>该参数配置为*时表示通配。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络访问标识符。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDNAIRGNPREF]] · DNAI区域优选规则（NRFDNAIRGNPREF）

## 使用实例

- 查询DNAI为huawei.com的区域优选规则。
  ```
  LST NRFDNAIRGNPREF: DNAI="huawei.com";
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
        数据网络名称  =  ims
  数据网络访问标识符  =  huawei.com
        区域优选规则  =  01-02:03-05
  (结果个数 = 1)
  ```
- 查询全部的DNAI区域优选规则。
  ```
  LST NRFDNAIRGNPREF:;
  %%LST NRFDNAIRGNPREF:;%%
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
        数据网络名称  =  ims
  数据网络访问标识符  =  huawei.com
        区域优选规则  =  01-02:03-05
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNAI区域优选规则（LST-NRFDNAIRGNPREF）_43660777.md`
