---
id: UNC@20.15.2@MMLCommand@LST S1APPARA
type: MMLCommand
name: LST S1APPARA（查询S1AP协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1APPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP协议参数
status: active
---

# LST S1APPARA（查询S1AP协议参数）

## 功能

**适用网元：MME**

此命令用于查看S1AP协议参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [S1AP协议参数（S1APPARA）](configobject/UNC/20.15.2/S1APPARA.md)

## 使用实例

执行如下命令查询S1AP参数:

LST S1APPARA:;

```
%%LST S1APPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 等待S1 Set up Request 消息定时器(s)  =  61
            重发MME配置更新定时器(s)  =  21
MME配置更新定时器超时重发次数(times)  =  1
                     防闪断定时器(s)  =  42
                  Reset超时定时器(s)  =  22
      Reset定时器超时重发次数(times)  =  2
                     Time to Wait(s)  =  60
                    SCTP数据绑定方式  =  不绑定
                  绑定等待时长（ms）  =  20
                    S1-U地址携带策略  =  先IPV4后IPV6
            SCTP消息重发抑制功能开关  =  开启
                        最大绑定包数  =  2
                        拥塞控制功能  =  开启
                    拥塞控制启控门限  =  4
                    拥塞控制恢复门限  =  5

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1AP协议参数(LST-S1APPARA)_26306068.md`
