---
id: UNC@20.15.2@MMLCommand@RMV SCTPLE
type: MMLCommand
name: RMV SCTPLE（删除SCTP本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCTPLE
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体
status: active
---

# RMV SCTPLE（删除SCTP本地实体）

## 功能

**适用网元：MME、AMF**

该命令用于删除SCTP链路本地实体。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，会导致和此本地实体相连的gNodeB上的用户业务中断。
- 如果待删除的SCTP本地实体所属的实体组被NGAP本地实体或SFGAP本地实体引用，且是最后一个SCTP本地实体则不能被删除。
- 如果待删除的SCTP本地实体所属的实体组被NGAP本地实体或SFGAP本地实体引用，且是最后一个用户类型为NONUE或者BOTH的则不能被删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPLEIDX | 链路本地实体索引 | 可选必选说明：必选参数<br>参数含义：待删除的SCTP链路本地实体号。<br>取值范围：0～1023<br>默认值：无<br>说明：可以通过<br>[**LST SCTPLE**](查询SCTP本地实体(LST SCTPLE)_11295784.md)<br>命令查看已有配置，确认所要删除的SCTP链路本地实体索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLE]] · SCTP本地实体（SCTPLE）

## 使用实例

删除链路本地实体号为1的SCTP链路：

```
%%RMV SCTPLE: SCTPLEIDX=1;%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCTP本地实体(RMV-SCTPLE)_11295837.md`
