---
id: UNC@20.15.2@MMLCommand@LST S1PAGINGCTRL
type: MMLCommand
name: LST S1PAGINGCTRL（查询S1寻呼策略控制表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1PAGINGCTRL
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
- S1寻呼策略管理
status: active
---

# LST S1PAGINGCTRL（查询S1寻呼策略控制表）

## 功能

**适用网元：MME**

此命令用于查询当前配置的S1寻呼策略。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1PAGINGCTRL]] · S1寻呼策略控制表（S1PAGINGCTRL）

## 使用实例

查询S1寻呼策略控制表：

LST S1PAGINGCTRL:;

```
%%LST S1PAGINGCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
    最近eNodeB开关  =  关
    邻接eNodeB开关  =  关
        最近TA开关  =  关
         SUB_T3413  =  3
  低移动性检查开关  =  关
    eNodeB粘性时长  =  60
        TA粘性时长  =  120
       ECT学习开关  =  关
      X2HO学习开关  =  关
      S1HO学习开关  =  关
邻接eNodeB老化时间  =  360
      全网寻呼开关  =  关
   SGs寻呼重发上限  =  15
  寻呼汇聚功能开关  =  开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1PAGINGCTRL.md`
