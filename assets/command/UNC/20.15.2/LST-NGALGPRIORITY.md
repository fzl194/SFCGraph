---
id: UNC@20.15.2@MMLCommand@LST NGALGPRIORITY
type: MMLCommand
name: LST NGALGPRIORITY（查询5G算法优先级属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGALGPRIORITY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 安全算法优先级管理
status: active
---

# LST NGALGPRIORITY（查询5G算法优先级属性）

## 功能

**适用NF：AMF**

该命令用于查询加密和完整性算法的优先级属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对何种类型的算法设置优先级属性，分加解密算法和完整性算法两种类型。<br>数据来源：全网规划<br>取值范围：<br>- “CIPH（加密算法）”：加密算法<br>- “INTE（完整性算法）”：完整性算法<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G算法优先级属性（NGALGPRIORITY）](configobject/UNC/20.15.2/NGALGPRIORITY.md)

## 使用实例

- 查询“算法类型”为“加密算法”的优先级属性，执行如下命令：
  ```
  %%LST NGALGPRIORITY: ALGTYPE=CIPH;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    算法类型  =  加密算法
    加密算法  =  SNOW 3G加密算法
  完整性算法  =  无效值
  算法优先级  =  0
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有算法优先级属性，执行如下命令：
  ```
  %%LST NGALGPRIORITY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  算法类型     加密算法         完整性算法         算法优先级          描述信息  

  加密算法     SNOW 3G加密算法  无效值             0                   NULL         
  完整性算法   无效值           SNOW 3G完整性算法  0                   NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G算法优先级属性（LST-NGALGPRIORITY）_09652999.md`
