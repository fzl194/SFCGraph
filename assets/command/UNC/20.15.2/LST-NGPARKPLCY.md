---
id: UNC@20.15.2@MMLCommand@LST NGPARKPLCY
type: MMLCommand
name: LST NGPARKPLCY（查询园区策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPARKPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 园区策略管理
status: active
---

# LST NGPARKPLCY（查询园区策略）

## 功能

**适用NF：AMF**

该命令用于查询园区策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARKID | 园区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识一个园区。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPARKPLCY]] · 园区策略（NGPARKPLCY）

## 使用实例

- 查询所有园区策略管理配置，执行如下命令：
  ```
  %%LST NGPARKPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  园区标识  区域编码  DNN群组标识  惯性运行开关  

  park      huawei    BIG_GROUP    关闭          
  park1     huawei1   BIG_GROUP    关闭          
  (结果个数 = 2)

  ---    END
  ```
- 查询园区标识为“park”的策略信息，执行如下命令：
  ```
  %%LST NGPARKPLCY: PARKID="park";%%
  RETCODE = 0  操作成功

  结果如下
  --------
      园区标识  =  park
      区域编码  =  huawei
   DNN群组标识  =  BIG_GROUP
  惯性运行开关  =  关闭
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPARKPLCY.md`
