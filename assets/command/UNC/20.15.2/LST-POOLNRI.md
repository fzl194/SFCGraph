---
id: UNC@20.15.2@MMLCommand@LST POOLNRI
type: MMLCommand
name: LST POOLNRI（查询POOL区NRI配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLNRI
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区NRI配置
status: active
---

# LST POOLNRI（查询POOL区NRI配置信息）

## 功能

**适用网元：SGSN**

此命令用于查询本POOL区内非本SGSN的NRI属性信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示POOL区标识。<br>取值范围：0～4095<br>默认值：无 |
| NRIV | NRI值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRI的值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>取值范围：0～1023<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLNRI]] · POOL区NRI配置信息（POOLNRI）

## 使用实例

查询本POOL区内所有非本SGSN的NRI属性信息：

LST POOLNRI:;

```
%%LST POOLNRI:;%%
RETCODE = 0  执行成功。

POOLNRI表
---------
                   POOL区标识  =  0
                        NRI值  =  1
                       IP类型  =  IPV4
               SGSN信令面地址  =  10.161.251.233
              SGSN信令面地址2  =  10.141.149.100
                     SGSN名称  =  SGSN50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POOLNRI.md`
