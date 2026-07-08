---
id: UNC@20.15.2@MMLCommand@LST NRFDNNNIRGNPREF
type: MMLCommand
name: LST NRFDNNNIRGNPREF（查询DNNNI区域优选规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDNNNIRGNPREF
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

# LST NRFDNNNIRGNPREF（查询DNNNI区域优选规则）

## 功能

**适用NF：NRF**

该命令用于查询DNNNI区域优选规则。该命令功能暂不生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNN网络标识。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNNNI区域优选规则（NRFDNNNIRGNPREF）](configobject/UNC/20.15.2/NRFDNNNIRGNPREF.md)

## 使用实例

- 查询DNNNI为huawei.com的区域优选规则。
  ```
  LST NRFDNNNIRGNPREF: DNNNI="huawei.com";
  %%LST NRFDNNNIRGNPREF: DNNNI="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
   DNN网络标识  =  huawei.com
  区域优选规则  =  01-02:03-04
  (结果个数 = 1)

  ---    END
  ```
- 查询全部的DNNNI区域优选规则。
  ```
  LST NRFDNNNIRGNPREF:;
  %%LST NRFDNNNIRGNPREF:;%%
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
   DNN网络标识  =  huawei.com
  区域优选规则  =  01-02:03-04
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNNNI区域优选规则（LST-NRFDNNNIRGNPREF）_93060774.md`
