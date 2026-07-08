---
id: UNC@20.15.2@MMLCommand@LST S1SMPROCTRL
type: MMLCommand
name: LST S1SMPROCTRL（查询S1模式SM流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1SMPROCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM流程管理
- S1模式SM流程控制参数
status: active
---

# LST S1SMPROCTRL（查询S1模式SM流程控制参数）

## 功能

**适用网元：MME**

该命令用于查询S1模式SM流程控制参数。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的流程类型。<br>数据来源：整网规划<br>取值范围：<br>- “PDN_CONNECTIVITY_PROC(PDN连接流程)”<br>- “BEARER_RESOURCE_ALLOCTION_PROC(承载资源分配流程)”<br>- “BEARER_RESOURCE_MOD_PROC(承载资源修改流程)”<br>- “DEDICATED_BEARER_ACT_PROC(专有承载建立流程)”<br>- “BEARER_MODIFICATION_PROC(承载修改流程)”<br>- “HSS_INIT_SUB_QOS_MOD_PROC(HSS发起的签约QoS修改流程)”<br>- “BEARER_DEACT_PROC(承载删除流程)”<br>- “ATTACH_BEARER_ACT_PROC(附着中缺省承载建立流程)”<br>默认值：无<br>说明：若不输入<br>“流程类型”<br>，则将显示所有流程类型的原因值、原因值组号，ECM-IDLE状态是否立即发起Qos修改流程，以及CBR、UBR的冲突处理模式。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1SMPROCTRL]] · S1模式SM流程控制参数（S1SMPROCTRL）

## 使用实例

查询S1模式SM流程控制参数：

LST S1SMPROCTRL:;

```
%%LST S1SMPROCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
           PDN连接拒绝原因值组号(SGW拒绝)  =  0
               PDN连接拒绝原因值(SGW超时)  =  0
      承载资源分配拒绝原因值组号(SGW拒绝)  =  0
          承载资源分配拒绝原因值(SGW超时)  =  0
      承载资源修改拒绝原因值组号(SGW拒绝)  =  0
          承载资源修改拒绝原因值(SGW超时)  =  0
附着中缺省承载建立拒绝原因值组号(SGW拒绝)  =  0
    附着中缺省承载建立拒绝原因值(SGW超时)  =  0
                          CBR冲突处理模式  =  拒绝
                          UBR冲突处理模式  =  拒绝
                      签约QoS变更判断策略  =  与正在使用的QoS比较
             ECM-IDLE状态立即发起修改流程  =  是
               重新激活类型的承载删除功能  =  重新激活方式
(结果个数 = 1)

---    END
```

查询流程类型为PDN连接流程的S1模式SM流程控制参数：

LST S1SMPROCTRL:PROT=PDN_CONNECTIVITY_PROC;

```
%%LST S1SMPROCTRL:PROT=PDN_CONNECTIVITY_PROC;%%

RETCODE = 0  操作成功。

操作结果如下
--------------
     PDN连接拒绝原因值组号(SGW拒绝)  =  0
         PDN连接拒绝原因值(SGW超时)  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式SM流程控制参数(LST-S1SMPROCTRL)_72345291.md`
