---
id: UNC@20.15.2@MMLCommand@LST QOSPROFILE
type: MMLCommand
name: LST QOSPROFILE（查询QoS描述配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSPROFILE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS模板
status: active
---

# LST QOSPROFILE（查询QoS描述配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询QosProfile的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoSProfile名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数不能和命令SET QOSGLOBAL的QosProfileName重复。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSPROFILE]] · QoS描述配置（QOSPROFILE）

## 使用实例

- 查询QosProfile名称为qp1的配置信息：
  ```
  %%LST QOSPROFILE: QOSPROFILENAME="qp1";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
             QoS Profile名  =  qp1
            EPS用户QoS索引  =  65535
         绑定Pre-R8用户QoS  =  不使能
          PreR8用户QoS索引  =  65535
            绑定EPS用户QoS  =  不使能
             5G用户QoS索引  =  65535
             绑定5G用户QoS  =  不使能
              最高业务级别  =  会话类
  超过最高业务级别时的处理  =  降级
  (结果个数 = 1)

  ---    END
  ```
- 查询整机的QosProfile的配置信息：
  ```
  %%LST QOSPROFILE:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  QoS Profile名  EPS用户QoS索引  绑定Pre-R8用户QoS  PreR8用户QoS索引  绑定EPS用户QoS  5G用户QoS索引  绑定5G用户QoS  最高业务级别  超过最高业务级别时的处理  

  qp1            65535           不使能             65535             不使能          65535          不使能         会话类        降级                      
  qp2            65535           不使能             65535             不使能          65535          不使能         会话类        降级                      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS描述配置（LST-QOSPROFILE）_09652691.md`
