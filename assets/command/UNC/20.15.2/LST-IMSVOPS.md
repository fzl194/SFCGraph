---
id: UNC@20.15.2@MMLCommand@LST IMSVOPS
type: MMLCommand
name: LST IMSVOPS（查询VoPS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSVOPS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- VoPS管理
status: active
---

# LST IMSVOPS（查询VoPS配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询SGSN和MME覆盖的RAN对PS域IMS（IP多媒体子系统）语音能力的支持情况，以及IMS语音业务相关的扩展功能。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSVOPS]] · VoPS配置（IMSVOPS）

## 使用实例

执行如下命令查询SGSN和MME侧对PS域IMS语音能力的支持情况:

LST IMSVOPS:;

```
%%LST IMSVOPS:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            SGSN侧全部支持PS域IMS语音  =  未指定
             MME侧全部支持PS域IMS语音  =  未指定
             支持IMS VoPS的TA获取模式  =  无效
                       跟踪区群组标识  =  NULL
基于语音域优选参数的SRVCC能力判断策略 =  NULL 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSVOPS.md`
