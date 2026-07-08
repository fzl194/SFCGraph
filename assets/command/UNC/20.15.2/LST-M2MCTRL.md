---
id: UNC@20.15.2@MMLCommand@LST M2MCTRL
type: MMLCommand
name: LST M2MCTRL（查询M2M控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MCTRL
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
- M2M管理
- M2M控制参数
status: active
---

# LST M2MCTRL（查询M2M控制参数）

## 功能

**适用网元：MME**

此命令用于查询当前配置的M2M控制参数。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MCTRL]] · M2M控制参数（M2MCTRL）

## 使用实例

查询M2M控制参数配置记录：

LST M2MCTRL:;

```
%%LST M2MCTRL:;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
        NB-S1模式寻呼窗口差值  =  相同
        WB-S1模式寻呼窗口差值  =  相同
                 eDRX寻呼优化  =  是
                   用户面偏好  =  使用UE偏好
               信令优先级指示  =  否
                     例外报告  =  否
             无线优化寻呼开关  =  关闭
           eNodeB属性检查开关  =  关闭
       eNodeB覆盖增强检查开关  =  关闭
               用户面建立优化  =  是
               NB-IoT DDN优化  =  否
            CE Mode B DDN优化  =  否
             缓存包数取值来源  =  使用本地配置
                     缓存包数  =  0
MME发起的CP到UP切换速率(次/秒) =  1
      NB-IoT用户支持多PDN连接  =  关闭
         下行数传延迟释放连接  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M2M控制参数(LST-M2MCTRL)_26145770.md`
