---
id: UNC@20.15.2@MMLCommand@LST NRFFRCAVLNF
type: MMLCommand
name: LST NRFFRCAVLNF（查询强制可用NF实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFFRCAVLNF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF服务能力参数管理
status: active
---

# LST NRFFRCAVLNF（查询强制可用NF实例）

## 功能

**适用NF：NRF**

该命令用于查询被设置为强制可用的NF以及该NF的忽略去注册开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示需要设置为强制可用的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFFRCAVLNF]] · 强制可用NF实例（NRFFRCAVLNF）

## 使用实例

- 查询所有配置的强制可用NF实例以及对应的忽略去注册开关状态：
  ```
  LST NRFFRCAVLNF:;
  %%LST NRFFRCAVLNF:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------
  NF实例标识                             忽略去注册开关

  123e4567-e89b-12d3-a456-426655440000   关闭
  223e4567-e89b-12d3-a456-426655440001   关闭 
  (结果个数 = 2)
  ```
- 查询标识为123e4567-e89b-12d3-a456-426655440000的NF实例是否强制可用以及是否打开忽略去注册开关，如果没有记录表明该NF实例不是强制可用。
  ```
  LST NRFFRCAVLNF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
  %%LST NRFFRCAVLNF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
  RETCODE = 0  操作成功

  结果如下
  -------------
      NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
  忽略去注册开关  =  关闭
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFFRCAVLNF.md`
